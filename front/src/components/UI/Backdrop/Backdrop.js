import React from 'react'

import './Backdrop.scss'

const backdrop = (props) =>{

    return(
        <div onClick ={props.backdropClicked} className = "backdrop"></div>
    )
}
export default backdrop