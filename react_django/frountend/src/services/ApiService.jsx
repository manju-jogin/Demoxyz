import axios from "axios"
import React from 'react'

function getstudent() {
  return axios.get('http://127.0.0.1:8000/students/')
  .then(res => {
    res.data

  })
}

export default ApiService
