import React from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import axios from "axios";

class MatchDetailForm extends React.Component {
  handleMatchIdSubmit = (event, request) => {
    const matchId = event.target.elements.matchId.value;

    axios
      .get("http://127.0.0.1:8000/api/match-details", {
        params: { match_id: matchId }
      })
      .then(res => console.log(res))
      .catch(error => console.log(error));
  };

  render() {
    return (
      <div>
        <form onSubmit={this.handleMatchIdSubmit}>
          <TextField
            name="matchId"
            label="Match ID"
            margin="normal"
            variant="outlined"
          />
          <br />
          <Button
            type="submit"
            variant="contained"
            size="large"
            color="primary"
          >
            Submit
          </Button>
        </form>
      </div>
    );
  }
}

export default MatchDetailForm;
