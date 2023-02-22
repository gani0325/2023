import React from "react";
class Customer extends React.Component {
    render() {
        return (
            <div>
                <h1>{this.props.name}</h1>
                <p>{this.props.birthday}</p>
                <p>{this.props.gender}</p>
            </div>
        );
    }
}

export default Customer;