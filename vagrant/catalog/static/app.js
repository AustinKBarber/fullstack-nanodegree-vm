import React from 'react';
import ReactDOM from 'react-dom';

class displayItems extends React.Component {
    render() {
        return <h1>Hello World</h1>;
    }
}

ReactDOM.render(
    <displayItems/>,
    document.getElementById('app')
);