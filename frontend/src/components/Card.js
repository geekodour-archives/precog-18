import React from 'react'

const Card = ({title,url}) => (
    <div className="card">
    <div className="card-image">
      <figure className="image is-4by3">
        <img src={url} alt=""/>
      </figure>
    </div>
    <div className="card-content">
      <div className="media">
        <div className="media-content">
          <p className="title is-4">{title}</p>
        </div>
      </div>
    </div>
  </div>
)

export default Card
