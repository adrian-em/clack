var React = require ('react');
var ReactDOM = require ('react-dom');

var Messages = React.createClass({
    render: function () {
        // this is empty  at first, avoid errors
        if (!this.props.messages) { return null }
        var messageList = this.props.messages.map(function (message, i) {
            var text = message.text;
            return (
                <div key={i} className="message">
                    <a href={"http://twitter.com/" + message.name + "/"} target="_blank" className="message_username"><img src={"http://twitter.com/" + message.name + "/profile_image"} className="message_profile_pic"/></a>
                    <a href={"http://twitter.com/" + message.name + "/"} target="_blank" className="message_username">{message.name}</a>
                    <span className="message_timestamp}">{new Date(message.time).toLocaleTimeString()}</span>
                    <span className="message_content" dangerouslySetInnerHTML={{ __html: text }}></span>
                </div>)
        });

        return (
            <div id="message-list">
                <div className="time-divide">
                    <span className="date"></span>
                </div>
                {messageList}
            </div>
        )
    }
});

module.exports = Messages;