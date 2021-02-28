import React, { useState, useEffect } from 'react';
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

import { getProcessedVideo } from '../../../api/api.helper'

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

    const [summary, setSummary] = useState(null);
    const [questions, setQuestions] = useState([]);
  
    	// useEffects
	useEffect(()=>{
		

	}, [])

    useEffect( () => {
		async function fetchAPI() {
			try {
                const id = localStorage.getItem("id");
                const responseData = await getProcessedVideo(id);
                setSummary(responseData.data.data.summary)
                setQuestions(responseData.data.data.questions)
			} catch(error) {
				console.error(error.toString());
			}
		}
		fetchAPI();
    }, []);
    
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
                        style={{
                            padding: '50px',
                            lineHeight: '30px'
                        }}
                    >
                        
                    </Typography>
                        {summary}
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
                        style={{
                            padding: '50px',
                            lineHeight: '30px'
                        }}
                    >
                        <ul>
                        {questions.map((question) => (
                            <li>{question}</li>
                        ))}
                        </ul>
                    </Typography>

                </CardContent>
            </Card>
        </div>



    );
}

