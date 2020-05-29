import React from 'react'
import {Link} from 'react-router-dom'
import HamburgerBtn from '../SideDrawer/HamburgerBtn'
import './Toolbar.scss'
import Logo from "../../../assets/Logo.png"

const toolbar = (props) => {

    return (
        <header className="toolbar">
            <nav className="toolbar__navigation">
                <div className = "toolbar__toggle-button">
                    <HamburgerBtn clicked={props.hamburgerClicked} />
                </div>
                <div className="toolbar__logo"><Link to="/"><img  width ="40px"src ={Logo}/></Link></div>
                <div className="toolbar__logo"><Link to="/">KMD Policy Tool</Link></div>
                <div className="space"></div>
                <div className="toolbar__navigation-items">
                    <ul>
                        <li><Link to ="/">Policies list</Link></li>
                        <li><Link to ="/new-politics">Add new Policy</Link></li>
                        <li><Link to ="/computer-list">Computer List</Link></li>
                        <li><Link to ="/new-computer">Add new Computer</Link></li>
                        
                    </ul>
                </div>
            </nav>
        </header>

    )
}

export default toolbar