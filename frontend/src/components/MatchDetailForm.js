import React from "react";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles(theme => ({
  margin: {
    margin: theme.spacing(1)
  }
}));

class MatchDetailForm extends React.Component {
  render() {
    return (
      <div>
        <form>
          <Button
            variant="contained"
            size="large"
            color="primary"
            className={classes.margin}
          >
            Large
          </Button>
        </form>
      </div>
    );
  }
}
