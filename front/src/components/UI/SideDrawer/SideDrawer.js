import React from 'react'
import {Link} from 'react-router-dom'
import './SideDrawer.scss'

const sideDrawer = (props) =>{
    let sideDrawerClasses = 'side-drawer'
    if(props.show){
        sideDrawerClasses = 'side-drawer open'
    }

    return(
        <nav className = {sideDrawerClasses}>
            <ul>
            <li><Link to ="/">Policies List</Link></li>
            <li><Link to ="/new-politics">Add new Policy</Link></li>
            <li><Link to ="/computer-list">Computer List</Link></li>
            <li><Link to ="/new-computer">Add new Computer</Link></li>
            </ul>
        </nav>
    )
}

export default sideDrawer 