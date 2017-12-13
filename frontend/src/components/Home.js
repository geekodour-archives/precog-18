import React from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'

import * as uiActions from '../actions/uiActions'

const Home = props => (
  <div>
    <section className="hero is-info">
    <div className="hero-body">
      <h1 className="title is-1">MemeHunter</h1>
      <div className="field has-addons">
        <div className="control">
          <input className="input" type="text" placeholder="Find a meme"/>
        </div>
        <div className="control">
          <a className="button is-warning"> Search </a>
        </div>
      </div>
    </div>
    </section>
    <section className="section">
      hh
    </section>
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
