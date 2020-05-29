import React from 'react';
import { Switch, Route } from 'react-router-dom'
import Toolbar from '../components/UI/Toolbar/Toolbar'
import SideDrawer from '../components/UI/SideDrawer/SideDrawer'
import Backdrop from '../components/UI/Backdrop/Backdrop'
import PageNotFound from '../components/UI/PageNotFound/PageNotFound'
import PolitictsList from '../components/PolitictsList/PolitictsList'
import ProjectDetails from '../components/PolitictsList/PoliticElement/ProjectDetails'
import NewPolitic from '../components/PolitictsList/NewPolitic'
import ComputerDetails from '../components/ComputerList/ComputerDetails'
import ComputerList from '../components/ComputerList/ComputerList'

import NewComputer from '../components/ComputerList/NewComputer'
import "./App.scss"
class App extends React.Component{
  state = {
    sideDrawerOpen: false
  }
  hamburgerClickHandler = () => {
    this.setState((prevState) => {
      return {
        sideDrawerOpen: !prevState.sideDrawerOpen
      }
    })
  }
  backdropClickHandler = () => {
    this.setState({ sideDrawerOpen: false })
  }
  render(){
    let backdrop = null
    if (this.state.sideDrawerOpen) {
      backdrop = <Backdrop backdropClicked={this.backdropClickHandler} />
    }
    return(
      <React.Fragment>
        <div className = "app_container">
          <Toolbar hamburgerClicked={this.hamburgerClickHandler} />
          <SideDrawer show={this.state.sideDrawerOpen} />
          {backdrop}
          <Switch>
            <Route path ="/" exact component ={PolitictsList} />
            <Route path ="/project/:id" component= {ProjectDetails}/>
            <Route path ="/new-politics" component = {NewPolitic}/>
            <Route path ="/computer-list" component ={ComputerList}/>
            <Route path ="/devices/:id" component ={ComputerDetails}/>
            <Route path="/new-computer" component = {NewComputer}/>
            <Route component = {PageNotFound}/>
          </Switch>
        </div>
      </React.Fragment>
    )
  }
}

export default App;
