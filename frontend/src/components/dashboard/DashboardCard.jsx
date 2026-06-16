function DashboardCard({ className = '', title, subtitle, children }) {
  const resolvedClassName = ['dashboard-card', className].filter(Boolean).join(' ')

  return (
    <section className={resolvedClassName}>
      <div className="dashboard-card__header">
        <h2 className="dashboard-card__title">{title}</h2>
        {subtitle ? <p className="dashboard-card__subtitle">{subtitle}</p> : null}
      </div>

      <div className="dashboard-card__body">{children}</div>
    </section>
  )
}

export default DashboardCard
