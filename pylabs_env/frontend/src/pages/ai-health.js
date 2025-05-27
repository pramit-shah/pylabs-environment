import { useEffect, useState } from 'react'
import axios from 'axios'

export default function AIHealth() {
  const [status, setStatus] = useState('Loading...')

  useEffect(() => {
    axios.get('http://localhost:5004/ai/health')
      .then(res => setStatus(res.data.status))
      .catch(() => setStatus('Error'))
  }, [])

  return <h1>AI Service Health: {status}</h1>
}
