// store.jsx
import { createStore, applyMiddleware, combineReducers } from 'redux';
import { thunk } from 'redux-thunk';
import adminHomeReducer from './reducers/AdminHomeReducer';

const rootReducer = combineReducers({
  adminHome: adminHomeReducer
});

const store = createStore(
    rootReducer,
    applyMiddleware(thunk)
);

export default store;
