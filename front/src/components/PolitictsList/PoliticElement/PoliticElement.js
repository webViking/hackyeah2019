import React from 'react'
import {Link} from 'react-router-dom'

const PoliticElement = (props) => {
    console.log(props)
    return (
        <div className="col-10 mx-auto col-md-5 col-lg-4 my-3">
        <div className="container">
            <div className="card">
                <div className="card-body">
                    <h5 className="card-title">{props.items.data.name}</h5>
                    <p className="card-text">Amount of rules: {props.items.data.rules.length}</p>
                    <h6 className="card-subtitle mb-2 text-muted">Amount of computers: {props.items.data.assigned_to.length}</h6>
                   {/* <p className="card-text">Cena</p>*/} 
                   <Link to ={{pathname:"/project/"+ props.items.id}}>
                        <button className="btn btn-warning  text-white mr-2 mt-2">Show details</button>
                   </Link>
                    
                
            
            </div>
        </div>
    </div>
    </div >
    )
}
export default PoliticElement