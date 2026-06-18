import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import client from '../api/client'
import DashboardCard from '../components/dashboard/DashboardCard'
import DashboardStatusPanel from '../components/dashboard/DashboardStatusPanel'
import './RiskHistoryPage.css'

function formatFeatureName(featureName) {
  return String(featureName)
    .split('_')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ')
}

function formatRiskScore(score) {
  return Number.isFinite(score) ? score.toFixed(3) : '--'
}

function formatGeneratedAt(dateString) {
  const date = new Date(dateString)

  if (Number.isNaN(date.getTime())) {
    return 'Unknown'
  }

  return new Intl.DateTimeFormat('en-US', {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(date)
}

function getRiskTone(level) {
  const normalized = String(level).toLowerCase()

  if (normalized === 'high') return 'high'
  if (normalized === 'medium') return 'medium'
  if (normalized === 'low') return 'low'

  return 'neutral'
}

function RiskHistoryPage() {
  const [status, setStatus] = useState('loading')
  const [history, setHistory] = useState([])
  const [trend, setTrend] = useState('stable')
  const [total, setTotal] = useState(0)
  const [error, setError] = useState('')

  const loadHistory = async () => {
    try {
      setStatus('loading')

      const response = await client.get('/api/v1/risk/history')

      const result = response.data

      setHistory(result.data || [])
      setTrend(result.trend || 'stable')
      setTotal(result.total || 0)

      if (!result.data || result.data.length === 0) {
        setStatus('empty')
      } else {
        setStatus('success')
      }
    } catch (err) {
      const message =
        err?.response?.data?.detail ||
        'Unable to load risk history.'

      setError(message)
      setStatus('error')
    }
  }

  useEffect(() => {
    loadHistory()
  }, [])

  return (
    <main className="dashboard-page risk-history-page">
      <section className="dashboard-page__hero">
        <div className="dashboard-page__hero-copy">
          <p className="dashboard-page__eyebrow">
            Prediction Timeline
          </p>

          <h1 className="dashboard-page__title">
            Risk History
          </h1>

          <p className="dashboard-page__lead">
            Review previous AI-generated risk assessments
            and monitor changes over time.
          </p>
        </div>

        <div className="dashboard-page__hero-badge dashboard-page__hero-badge--neutral">
          {total} Risk Assessments
        </div>
      </section>

      {status === 'loading' && (
        <DashboardStatusPanel
          tone="loading"
          title="Loading Risk History"
          message="Fetching previous assessments from VitalGuard."
        />
      )}

      {status === 'error' && (
        <DashboardStatusPanel
          tone="error"
          title="Unable to load risk history"
          message={error}
          actionLabel="Try Again"
          onAction={loadHistory}
        />
      )}

      {status === 'empty' && (
        <DashboardStatusPanel
          tone="empty"
          title="No risk assessments yet"
          message="Start by logging a set of vitals."
          actionLabel="Add Vitals"
          actionTo="/add-vitals"
        />
      )}

      {status === 'success' && (
        <>
          <section className="dashboard-grid risk-summary-grid">
            <DashboardCard
              className="dashboard-card--overview"
              title="Trend"
              subtitle="Overall direction of your risk history"
            >
              <div className="risk-overview">
                <div>
                  <div className="trend-pill trend-pill--stable">
                     Stable
                  </div>
                  <p className="risk-overview__caption">
                    Your risk level has remained consistant across recent assessments.
                  </p>
                </div>
              </div>
            </DashboardCard>

            <DashboardCard
              className="dashboard-card--metadata"
              title="Total Records"
              subtitle="Stored assessments"
            >
              <div className="metadata-block">
                <p className="metadata-block__value">
                  {total}
                </p>

                <p className= "metadata-block__label">
                  Assessments Logged
                </p>

                <p className="dashboard-card__subtitle">
                  Track how your health risk evolves over time.
                </p>
              </div>
            </DashboardCard>
          </section>

          <section className="history-list">
            {history.map((item) => {
              const riskTone = getRiskTone(item.level)

              return (
                <DashboardCard
                  key={item.id}
                  className="history-card"
                  title="Risk Assessment"
                  subtitle={formatGeneratedAt(item.generated_at)}
                >
                  <div className="history-card__header">
                    <div>
                      <p className="history-card__score">
                        {formatRiskScore(item.risk_score)}
                      </p>

                      <p className="history-card__label">
                        Risk Score
                      </p>
                    </div>

                    <div
                      className={`risk-level-pill risk-level-pill--${riskTone}`}
                    >
                      {String(item.level).toUpperCase()} RISK
                    </div>
                  </div>

                  <div className="factor-badges">
                    {item.top_factors?.map((factor) => (
                      <span
                        key={factor}
                        className="factor-badge"
                      >
                        {formatFeatureName(factor)}
                      </span>
                    ))}
                  </div>

                  <p className="history-card__explanation">
                    {item.explanation}
                  </p>

                  <p className="history-card__footer">
                    Generated on{' '}
                    {formatGeneratedAt(item.generated_at)}
                  </p>
                </DashboardCard>
              )
            })}
          </section>

          <div className="history-actions">
            <Link to="/add-vitals" className="dashboard-status__action">
              Add New Vitals
            </Link>
          </div>
        </>
      )}
    </main>
  )
}

export default RiskHistoryPage