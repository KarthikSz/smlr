import axios, { post, get } from 'axios';

axios.defaults.validateStatus = () => true;
axios.defaults.withCredentials = true;

// Configurations
const config = {
	headers: {
		'content-type': 'multipart/form-data'
	}
};

const serverURL = 'http://localhost:8000/api';

const uploadVideo = async (file) => {
	const formData = new FormData();
	formData.append('video', file);
	return post(`${serverURL}/upload/video/`, formData, config);
};

const viewAllProcessedVideos = async () => {
	return get(`${serverURL}/processed/`);
};

const getProcessedVideo = async (id) => {
	return get(`${serverURL}/processed/info`, {params: {id}});
};

export {
    uploadVideo,
	viewAllProcessedVideos,
	getProcessedVideo
};
