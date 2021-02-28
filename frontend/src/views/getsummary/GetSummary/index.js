import React from 'react';
import {
    Box,
    Container,
} from '@material-ui/core';
import Page from 'src/components/Page';

import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
    root: {
        minWidth: 275,
    },
    bullet: {
        display: 'inline-block',
        margin: '0 2px',
        transform: 'scale(0.8)',
    },
    title: {
        fontSize: 14,
    },
    pos: {
        marginBottom: 12,
    },
});

export default function GetSummary() {
    const classes = useStyles();
    const bull = <span className={classes.bullet}>•</span>;

    return (
        <div>
            <Card className={classes.root} variant="outlined">
                <CardContent>
                    <Typography
                        align="center"
                        color="textPrimary"
                        gutterBottom
                        variant="h4"
                    >
                        SUMMARY
                    </Typography>
                    <Typography
                        align="center"
                        color="textPrimary"
                        variant="body1"
                    >
                        fetched summary
                    </Typography>


                </CardContent>
            </Card>
            <Card className={classes.root} variant="outlined">
                <CardContent>
                    <Typography
                        align="center"
                        color="textPrimary"
                        gutterBottom
                        variant="h4"
                    >
                        IMPORTANT QUESTIONS
                    </Typography>
                    <Typography
                        align="center"
                        color="textPrimary"
                        variant="body1"
                    >
                        fetch questions
                    </Typography>

                </CardContent>
            </Card>
        </div>



    );
}

