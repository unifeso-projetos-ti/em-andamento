import { DateRangePicker } from '@nextui-org/date-picker'
import { ChartBar } from 'src/components/Dashboard/chart-bar'
import MovementTable from 'src/components/Dashboard/movement-table'
import { SummaryCard } from 'src/components/Dashboard/summary-card'
import { ISummaryCard } from 'src/models/summary-card'

export function Dashboard() {
  const dataMonth: ISummaryCard[] = [
    {
      title: 'Receitas totais',
      total: 20000,
      percentage: 21,
      text_percentage: 'do mês passado',
    },
    {
      title: 'Gastos totais',
      total: 3000,
      percentage: 50,
      text_percentage: 'do mês passado',
    },
    {
      title: 'Média geral',
      total: 21000,
      percentage: 50,
      text_percentage: 'do mês passado',
    },
  ]
  return (
    <main className="w-full p-4">
      <div className="flex flex-col gap-8">
        <div className="w-full flex items-center justify-between">
          <header>
            <h1>Dashboard</h1>
          </header>

          <DateRangePicker label="Coloque o intervalo" className="max-w-xs" />
        </div>
        <div className="flex items-center gap-4">
          {dataMonth.map((data, index) => (
            <SummaryCard
              key={index}
              title={data.title}
              total={data.total}
              percentage={data.percentage}
              text_percentage={data.text_percentage}
            />
          ))}
        </div>
        <div className="w-full items-end gap-8 flex">
          <div className="w-[60%] bg-white p-4 rounded-large">
            <ChartBar />
          </div>
          <div className="w-[40%]">
            <MovementTable />
          </div>
        </div>
      </div>
    </main>
  )
}

export default Dashboard
