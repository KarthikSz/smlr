import React, { useState } from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import {
  Box,
  Button,
  Card,
  CardContent,
  CardHeader,
  Divider,
  TextField,
  makeStyles
} from '@material-ui/core';
import CircularProgress from '@material-ui/core/CircularProgress';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import Dialog from '@material-ui/core/Dialog';

import { uploadVideo } from '../../../api/api.helper';

import './Password.css'

const useStyles = makeStyles(({
  root: {}
}));

const Password = ({ className, ...rest }) => {
  const classes = useStyles();
  const [values, setValues] = useState({
    password: '',
    confirm: ''
  });
  const [videoLocation, setVideoLocation] = useState(null);
  const [open, setOpen] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleChange = (event) => {
    setValues({
      ...values,
      [event.target.name]: event.target.value
    });
  };

  const validateFile = async (file) => {
		const allowedFileTypesRE = /mp4|avi/;
		// File size limit: 100 MB
		if(file.size > 1000000* 100){
			console.error('File size should be less than 100MB.');
			return false;
		}
		else if(!allowedFileTypesRE.test(file.type)){
			console.error('File type should be in mp4 or avi format.');
			return false;
		}
		return true;
  };
  
  const handleFileChange = async (e, field) => {
    if(await validateFile(e.target.files[0])){
      setVideoLocation(e.target.files[0]);
    } else {
      setVideoLocation(null);
    }
  };

  const handleFileUpload = async (e, field) => {
    setOpen(true);
    const uploadResponse = await uploadVideo(videoLocation);
    if(uploadResponse.data.status_code==200){
      setVideoLocation(uploadResponse.data.data);
      console.log(uploadResponse.data);
    }
    else{
      console.log(uploadResponse.data);
    }
  };

  return (
    <div>
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            <CircularProgress />

          </DialogContentText>
        </DialogContent>
      </Dialog>
      <form
        className={clsx(classes.root, className)}
        {...rest}
      >
        <Card>
          <CardHeader
            subheader="Upload Video"
            title="Process Lectures"
          />
          <Divider />
          <CardContent>
            {/* <TextField
              fullWidth
              label="Password"
              margin="normal"
              name="password"
              onChange={handleChange}
              type="password"
              value={values.password}
              variant="outlined"
            /> */}

            <Box>
              <div class="form-group file-area">
                    {/* <label for="images">Images <span>Your images should be at least 400x300 wide</span></label> */}
                <input
                  type="file"
                  name="video"
                  id="video"
                  required="required"
                  onChange={(e) => { e.persist(); handleFileChange(e, 'video'); }}
                />
                <div class="file-dummy">
                  <div class="success">Great, your file is selected.</div>
                  <div class="default">Select a video to upload</div>
                </div>
              </div>  
              {/* <Button variant="contained" component="label" className={classes.button}>
                Choose File
                <input
                  type="file"
                  onChange={(e) => { e.persist(); handleFileChange(e, 'video'); }}
                  style={{ display: 'none' }}
                />
              </Button> */}
            </Box>
          </CardContent>
          <Divider />
          <Box
            display="flex"
            justifyContent="flex-end"
            p={2}
          >
            <Button
              color="primary"
              variant="contained"
              onClick={() => handleFileUpload('video')}
            >
              Upload
            </Button>
          </Box>
        </Card>
      </form>
    </div>
  );
};

Password.propTypes = {
  className: PropTypes.string
};

export default Password;
