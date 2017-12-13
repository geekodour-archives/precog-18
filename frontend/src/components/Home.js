import React from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'

import * as uiActions from '../actions/uiActions'

const Home = props => (
  <div>
    <h1>Home</h1>
    <p>Welcome home!</p>
    <button onClick={props.uiActions.dimToggle}>Toggle</button>
    <pre>{JSON.stringify(props.ui)}</pre>
  </div>
)

const mapStateToProps = state => (
  {
    ui: state.ui
  }
);

const mapDispatchToProps = dispatch => (
  {
    uiActions: bindActionCreators(uiActions, dispatch)
  }
);

export default connect( mapStateToProps, mapDispatchToProps)(Home)
