import React from 'react'

const PoliticRule = (props) =>{
   console.log(props)
   
    return(
        <div className ="col-12">{props.count}{". "}{props.el.name}</div>
    )
}
export default PoliticRule