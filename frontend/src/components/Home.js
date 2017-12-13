import React from 'react'
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'

import * as uiActions from '../actions/uiActions'
import Card from './Card'

const Home = props => {
  const handleSubmit = () => {
    let i = document.getElementsByName('search_input')[0]
    props.uiActions.searchMeme(i.value)
  }
  return(
  <div>
    <section className="hero is-info">
    <div className="hero-body">
      <h1 className="title is-1">MemeHunter</h1>
      <div className="field has-addons">
        <div className="control">
          <input name="search_input" className="input" type="text" placeholder="Find a meme"/>
        </div>
        <div className="control">
          <a className="button is-warning" onClick={handleSubmit}> Search </a>
        </div>
      </div>
    </div>
    </section>
    <section className="section">
      <div className="columns is-multiline">
        { props.ui.memeList.map(m=>(
          <div key={m.id} className="column is-4"> <Card title={m.title} url={m.url}/> </div>
          ))
        }
      </div>
    </section>
  </div>
  )
}

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
