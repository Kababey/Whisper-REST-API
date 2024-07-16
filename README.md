# Whisper-REST-API
Whisper REST API is made by using Fast API

Whisper outperforms other models in terms of performance. In this task, we will use Python to infer OpenAI's Whisper model and create a REST API using the FastAPI framework.

If you dont have FFMPEG you may see errors. To check it:
``ffmpeg -version``
If not follow the link:
[Geeksforgeeks ffmpeg on windows](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/) 

Whisper installation:```pip install git+https://github.com/openai/whisper.git```  OR:          ```pip install whisper```

Go to your project folder
Necessary commands:
```
python3 -m venv whisper-env 
whisper-env/bin/activate 
pip install fastapi uvicorn pydantic whisper 
```
We are ready to start the API:
```uvicorn main:app --reload ```
                      
You can follow steps to test your API with Swagger UI shown below:

We need to create two endpoints:

/inferencePath

Upload a multimedia file in MP3, WAV, or MP4 format to a specified path, which is then passed to this endpoint.
The file at the given path is read and converted to text.
The resulting text is returned in both .txt and .srt formats in the response body.

Enter the docs: 
http://127.0.0.1:8000/docs

![image](https://github.com/user-attachments/assets/05ac4ba5-8ac6-4c2d-b337-a378462c73c8)

![image](https://github.com/user-attachments/assets/592c2611-987d-4657-9e9e-e00aa164f141)

![image](https://github.com/user-attachments/assets/8a217457-7c65-44bb-a425-faecdfd5378a)


/inferenceRaw

Upload a multimedia file in MP3, WAV, or MP4 format directly to this endpoint as the request body.
The uploaded file is converted to text.
The resulting text is returned in both .txt and .srt formats in the response body.

![image](https://github.com/user-attachments/assets/10b8f03d-a5d2-4e51-9602-f9d089a00ffe)

After using one of the two methods correctly, there will be srt and txt files in the temp folder created.
There is an example of transcription created by this API in the test_results folder

## Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI Whisper Model](https://github.com/openai/whisper)
- [Python Official Documentation](https://docs.python.org/3/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Virtual Environments in Python](https://docs.python.org/3/library/venv.html)
