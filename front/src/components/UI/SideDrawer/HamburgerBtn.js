import React from 'react'
import './HamburgerBtn.scss'

const hamburgerBtn = (props) =>{

    return(
        <button className = "toggle-button" onClick = {props.clicked}>
            <div className = "toggle-button__line"></div>
            <div className = "toggle-button__line"></div>
            <div className = "toggle-button__line"></div>
        </button>
    )
}

export default hamburgerBtn