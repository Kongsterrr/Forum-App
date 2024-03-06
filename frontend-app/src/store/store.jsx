// store.jsx
import { createStore, applyMiddleware, combineReducers } from 'redux';
import { thunk } from 'redux-thunk';
import adminHomeReducer from './reducers/AdminHomeReducer';
import userManagementReducer from './reducers/UserManagementReducer';
import loginReducer from './reducers/LoginReducer';
import MessageManagementReducer from './reducers/MessageManagementReducer';
import ContactAdminReducer from './reducers/ContactAdminReducer';

const rootReducer = combineReducers({
  userLogin: loginReducer,
  adminHome: adminHomeReducer,
  userManage: userManagementReducer,
  messages: MessageManagementReducer,
  contact: ContactAdminReducer
});

const initialState = {
  messages: [],
};

const store = createStore(
    rootReducer,
    initialState,
    applyMiddleware(thunk)
);

export default store;
