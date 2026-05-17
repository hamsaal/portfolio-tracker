import { useState, useEffect } from 'react'
import axios from 'axios'

function AssetList() {
    const [assets, setAssets] = useState([])
    const [loading, setLoading] = useState(true)

    useEffect(() => {
        axios.get('http://localhost:8000/api/assets/')
            .then(response => {
                setAssets(response.data)
                setLoading(false)
            })
    }, [])

    if (loading) return <p>Loading...</p>

    return (
        <div>
            <h2>Assets</h2>
            {assets.map(asset => (
                <div key={asset.id}>
                    <strong>{asset.ticker}</strong> — {asset.name} ({asset.asset_type})
                </div>
            ))}
        </div>
    )
}

export default AssetList