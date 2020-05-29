import { createStore, applyMiddleware, combineReducers, compose  } from 'redux';
import thunk from 'redux-thunk';

import mainReducer from './reducers/mainReducer'

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const rootReducer = combineReducers({
    products: mainReducer,
})

export const configuredStore =  createStore(
        rootReducer,
       composeEnhancers(applyMiddleware(thunk))
)
