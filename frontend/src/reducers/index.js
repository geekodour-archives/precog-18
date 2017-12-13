import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'

// import reducers
import ui from './uiReducer'


// setup apollo redux client
//const networkInterface = createNetworkInterface({ uri: 'https://api.graph.cool/simple/v1/insta-prod' });
//export const client = new ApolloClient({ networkInterface });

export default combineReducers({
  ui,
  routing: routerReducer
})
