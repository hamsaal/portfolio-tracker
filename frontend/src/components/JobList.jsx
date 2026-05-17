import { useState, useEffect } from 'react'
import api from '../api'
import './JobList.css'

function JobList() {
    const [jobs, setJobs] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        api.get('/jobs/')
            .then(response => {
                setJobs(response.data)
                setLoading(false)
            })
    }, [])

    if (loading) return <p className="loading">Loading...</p>

    return (
        <div className="panel">
            <h2>Jobs</h2>
            <div className="job-list">
                {jobs.map(job => (
                    <div key={job.id} className="job-card">
                        <div className="job-info">
                            <span className="job-name">{job.name}</span>
                            <span className="job-meta">
                                {job.device_name} · {job.submitted_by}
                            </span>
                        </div>
                        <div className="job-right">
                            <span className={`status-badge status-${job.status}`}>
                                {job.status}
                            </span>
                            <span className="job-duration">
                                {job.duration ?? 'In progress'}
                            </span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default JobList