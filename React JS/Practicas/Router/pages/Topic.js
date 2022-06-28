import React from 'react';
import { useParams } from 'react-router-dom';

const Topic = () => {

    let {topic} = useParams();

  return (
    <div>
        <h4>{topic}</h4>
        <p>docs de {topic}</p>
    </div>
  )
}

export default Topic;