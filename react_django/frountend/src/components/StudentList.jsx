import React, { useEffect, useState } from 'react'
import{getstudent} from '../services/ApiService'


function StudentList() {
const [students,setStudents] = useState([])

useEffect(() => {
   let mount = true
   getstudent()
   .then(res => {
    setStudents(res)
    return() => mount = false
   })
},[])


  return (
    <div>
      <h2>student Lists</h2>
      <table>
        <thead>
            <tr>
                <td>Fristname</td>
                <td>Lasttname</td>
                <td>Standrad</td>
                <td>RollNumber</td>
                <td>DOB</td>
                <td>Phone</td>
                <td>Gender</td>
            </tr>
        </thead>
        <tbody>
            {students.map(x => {
               return <tr key={x.student_id}>
                <td>{x.Fristname}</td>
                <td>{x.Lasttname}</td>
                <td>{x.Standrad}</td>
                <td>{x.RollNumber}</td>
                <td>{x.DOB}</td>
                <td>{x.Phone}</td>
                <td>{x.Gender}</td>
            </tr>

            })}
            
        </tbody>
        
      </table>
    </div>
  )
}

export default StudentList
