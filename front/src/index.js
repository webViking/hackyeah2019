import React from 'react';
import ReactDOM from 'react-dom';
import App from './containers/App';
import { BrowserRouter } from 'react-router-dom';
import * as serviceWorker from './serviceWorker';
import { Provider } from 'react-redux'
import {configuredStore} from './redux/storeConfiguration'

const app = (
    <Provider store= {configuredStore}>
    <BrowserRouter>
        <App/>
    </BrowserRouter>
    </Provider>
)
ReactDOM.render(app, document.getElementById('root'));

serviceWorker.unregister();
