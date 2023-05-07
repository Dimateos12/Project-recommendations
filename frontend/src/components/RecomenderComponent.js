import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import { Grid } from "@material-ui/core";
import Box from "@mui/material/Box";
import axios from "axios";

export default function RecomenderComponent(props) {
  const [open, setOpen] = React.useState(false);
  const handleClickOpen = () => {
    setOpen(true);
  };
  const API_URL = "http://localhost:8000/api/";
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);

    const stateTemp = {
      first_name: data.get("first_name"),
      last_name: data.get("last_name"),
      email: data.get("email"),
    };
    console.log(stateTemp);
    axios.post(API_URL + "advertisements/details/" + props.id + "/", stateTemp).then((response) => {
      window.location.reload(true);
    });

    setOpen(false);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <div>
      <Button variant="outlined" onClick={handleClickOpen}>
        Poleć !
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Formularz Polecajacy</DialogTitle>
        <DialogContent>
          <DialogContentText>
            Polec swojego znajomego, rodzine by otrzymac punkty.
          </DialogContentText>
          <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <Grid container direction={"column"} spacing={2}>
              <Grid item> </Grid>
              <Grid item>
                <TextField
                  required
                  id="first_name"
                  name="first_name"
                  label="Required"
                  defaultValue="Imie"
                />
              </Grid>
              <Grid item>
                <TextField
                  required
                  id="last_name"
                  name="last_name"
                  label="Required"
                  defaultValue="Nazwisko"
                />
              </Grid>
              <Grid item>
                <TextField required id="email" name="email" label="Required" defaultValue="Email" />
              </Grid>
              <Grid item>
                <Button style={{ marginRight: "20px" }} onClick={handleClose}>
                  Anuluj
                </Button>
                <Button type="submit">Poleć!</Button>
              </Grid>
            </Grid>
          </Box>
        </DialogContent>
        <DialogActions></DialogActions>
      </Dialog>
    </div>
  );
}