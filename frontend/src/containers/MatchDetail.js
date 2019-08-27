import React from "react";
import axios from "axios";

class MatchDetail extends React.Component {
  state = {
    matchDetail: {}
  };

  componentDidMount() {
    axios.get(`http://127.0.0.1:8000/api/match-details`).then(res => {
      this.setState({
        matchDetail: res.data
      });
    });
  }

  render() {
    return 1;
  }
}

export default MatchDetail;
