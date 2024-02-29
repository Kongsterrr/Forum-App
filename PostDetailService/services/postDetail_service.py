import requests

class PostDetailService:
    def __init__(self):
        self.post_and_reply_service_url = 'http://127.0.0.1:5000/post_and_reply'
        self.user_service_url = 'http://127.0.0.1:5000/users'

    def get_post_detail(self, post_id):
        # Fetch the post details
        post_response = requests.get(f'{self.post_and_reply_service_url}/{post_id}')
        if post_response.status_code != 200:
            return {'error': 'Post not found or service unavailable'}
        post_data = post_response.json()

        # Fetch the user details
        user_id = post_data['userId']
        user_response = requests.get(f'{self.user_service_url}/{user_id}')
        if user_response.status_code != 200:
            return {'error': 'User details not found or service unavailable'}
        user_data = user_response.json()

        # Fetch the replies for the post
        reply_response = requests.get(f'{self.post_and_reply_service_url}/{post_id}/reply')
        if reply_response.status_code != 200:
            replies = []

        reply_data_container = reply_response.json()
        reply_data = reply_data_container.get('replies', [])

        replies_list = []
        for reply in reply_data:
            user_id = reply['userId']
            try:
                user_response = requests.get(f'{self.user_service_url}/{user_id}')
                if user_response.status_code == 200:
                    reply_user_data = user_response.json()
                    replies_list.append({
                        'firstName': reply_user_data['firstName'],
                        'lastName': reply_user_data['lastName'],
                        'profileImage': reply_user_data.get('profileImage'),
                        'comment': reply['comment'],
                        'dateCreated': reply['dateCreated'],
                    })
                else:
                    replies_list.append({
                        'error': f'User details for userId {user_id} could not be fetched',
                        'comment': reply['comment'],
                        'dateCreated': reply['dateCreated'],
                    })
            except ValueError:
                replies_list.append({'error': f'Invalid JSON response for user with ID {user_id}'})

        aggregated_data = {
            'postId': post_data['postId'],
            'title': post_data['title'],
            'content': post_data['content'],
            'user': {
                'firstName': user_data['firstName'],
                'lastName': user_data['lastName'],
                'profileImage': user_data.get('profileImage'),
            },
            'dateCreated': post_data['dateCreated'],
            'dateModified': post_data.get('dateModified'),
            'replies': replies_list
        }

        return aggregated_data


    def get_user_home(self):
        try:
            post_response = requests.get(f'{self.post_and_reply_service_url}/published-post')
            if post_response.status_code == 200:
                posts_data = post_response.json()
            else:
                return {'error': f'Failed to fetch posts, status code: {post_response.status_code}'}
        except ValueError:
            return {'error': 'Invalid JSON response from posts service'}

        aggregated_data_list = []

        for post in posts_data:
            user_id = post['userId']
            try:
                user_response = requests.get(f'{self.user_service_url}/{user_id}')
                if user_response.status_code == 200:
                    user_data = user_response.json()
                    aggregated_data = {
                        'firstName': user_data.get('firstName'),
                        'lastName': user_data.get('lastName'),
                        'date': post['dateModified'] if post.get('dateModified') else post['dateCreated'],
                        'title': post['title'],
                    }
                    aggregated_data_list.append(aggregated_data)
                else:
                    aggregated_data_list.append({
                        'error': f'User details for userId {user_id} could not be fetched, status code: {user_response.status_code}'
                    })
            except ValueError:
                aggregated_data_list.append({'error': f'Invalid JSON response for user with ID {user_id}'})

        return aggregated_data_list
