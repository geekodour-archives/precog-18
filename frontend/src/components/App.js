import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import Home from './Home'
import About from './About'

const App = props => (
  <Router>
  <div>
    <nav>
      <Link to="/">Home</Link>
      {/*<Link to="/about-us">About</Link>*/}
    </nav>
    <div class="container">
    <Route exact path="/" component={Home} />
    <Route exact path="/about-us" component={About} />
    <Route exact path="/cool" component={Home} />
    </div>
  </div>
  </Router>
)

export default App;
