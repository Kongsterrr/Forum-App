// store.jsx
import { createStore, applyMiddleware, combineReducers } from 'redux';
import { thunk } from 'redux-thunk';
import adminHomeReducer from './reducers/AdminHomeReducer';
import userManagementReducer from './reducers/UserManagementReducer';
import loginReducer from './reducers/LoginReducer';


const rootReducer = combineReducers({
  userLogin: loginReducer,
  adminHome: adminHomeReducer,
  userManage: userManagementReducer
});

const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

export default store;
