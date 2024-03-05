// store.jsx
import { createStore, applyMiddleware, combineReducers } from 'redux';
import { thunk } from 'redux-thunk';
import adminHomeReducer from './reducers/AdminHomeReducer';
import userManagementReducer from './reducers/UserManagementReducer';


const rootReducer = combineReducers({
  adminHome: adminHomeReducer,
  userManage: userManagementReducer
});

const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

export default store;
