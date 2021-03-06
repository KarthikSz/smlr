import React, { useEffect } from 'react';
import {useNavigate} from 'react-router-dom';


import PropTypes from 'prop-types';
import clsx from 'clsx';
import {
  Avatar,
  Box,
  Card,
  CardContent,
  Divider,
  Grid,
  Typography,
  makeStyles,
  CardActionArea, CardMedia
} from '@material-ui/core';
import AccessTimeIcon from '@material-ui/icons/AccessTime';
import GetAppIcon from '@material-ui/icons/GetApp';
import {viewAllProcessedVideos} from '../../../api/api.helper';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexDirection: 'column'
  },
  statsItem: {
    alignItems: 'center',
    display: 'flex'
  },
  media: {
    height: 0,
    paddingTop: '56.25%', // 16:9
  },
  statsIcon: {
    marginRight: theme.spacing(1)
  }
}));


  

  const ProductCard = ({ className, product, ...rest }) => {
  const classes = useStyles();
  const navigate = useNavigate();

  return (
   
    <Card
      className={clsx(classes.root, className)}
      {...rest}
    >
      <CardActionArea 
      onClick = { () => {
        navigate('/app/getsummary/')
      }}
      >
      <CardContent>
        <Box
          display="flex"
          justifyContent="center"
          mb={3}
        >
          
        </Box>
        <Typography
          align="center"
          color="textPrimary"
          gutterBottom
          variant="h4"
        >
          {product.title}
        </Typography>
        <CardMedia
          className={classes.media}
          image={product.image}
          
        />
      </CardContent>
      <Box flexGrow={1} />
      
      
      </CardActionArea>
    </Card>
  );
};

ProductCard.propTypes = {
  className: PropTypes.string,
  product: PropTypes.object.isRequired
};

export default ProductCard;
