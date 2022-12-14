const API_URL="http://127.0.0.1:8000/api/model/";

export const listModels = async () =>{
     return await fetch(API_URL);
};