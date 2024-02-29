import logo from './logo.svg';
import './App.css';
// import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import MessageManagementPage from "./components/MessageManagementPage/MessageManagementPage";

function App() {
  return (
      // <Router>
      //   <div className="App">
      //     <Switch>
      //       <Route exact path="/admin/messages" component={MessageManagementPage} />
      //     </Switch>
      //   </div>
      // </Router>
      <MessageManagementPage />
  );
}

export default App;
