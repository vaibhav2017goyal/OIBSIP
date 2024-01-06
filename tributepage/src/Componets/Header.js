import React from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCirclePlay } from "@fortawesome/free-solid-svg-icons";

const Header = () => {
  return (
    <header className="App-header">
        <div>
        <h1>Steve Jobs <br/></h1>
        <h2>1955-2011</h2>
        <div className='Icon'>
          <br/>
        <FontAwesomeIcon  icon={faCirclePlay} />
        <br/>
        <br/>
        </div>
        </div>
      </header>
  )
}

export default Header