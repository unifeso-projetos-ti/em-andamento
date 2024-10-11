'use client'

import { Bar, BarChart, CartesianGrid, XAxis } from 'recharts'
import { Card, CardContent } from 'src/components/ui/card'
import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from 'src/components/ui/chart'

const chartData = [
  { month: 'Janeiro', salary: 3525.0, costs: 1200.0 },
  { month: 'Fevereiro', salary: 3384.0, costs: 950.0 },
  { month: 'Março', salary: 4400.0, costs: 1750.0 },
  { month: 'Abril', salary: 4200.0, costs: 1300.0 },
  { month: 'Maio', salary: 4400.0, costs: 1600.0 },
  { month: 'Junho', salary: 4200.0, costs: 1100.0 },
  { month: 'Julho', salary: 5350.0, costs: 2000.0 },
  { month: 'Agosto', salary: 5350.0, costs: 2100.0 },
  { month: 'Setembro', salary: 5350.0, costs: 1800.0 },
  { month: 'Outubro', salary: 5350.0, costs: 1900.0 },
  { month: 'Novembro', salary: 5350.0, costs: 1700.0 },
  { month: 'Dezembro', salary: 5350.0, costs: 2200.0 },
]

const chartConfig = {
  salary: {
    label: 'Salário',
    color: 'hsl(var(--chart-1))',
  },
  costs: {
    label: 'Custos',
    color: 'hsl(var(--chart-2))',
  },
} satisfies ChartConfig

export function ChartBar() {
  return (
    <Card className="border-0">
      <CardContent>
        <ChartContainer config={chartConfig}>
          <BarChart accessibilityLayer data={chartData}>
            <CartesianGrid vertical={false} />
            <XAxis
              dataKey="month"
              tickLine={false}
              tickMargin={10}
              axisLine={false}
              tickFormatter={(value) => value.slice(0, 3)}
            />
            <ChartTooltip
              cursor={false}
              content={<ChartTooltipContent indicator="dashed" />}
            />
            <Bar dataKey="salary" fill="var(--color-salary)" radius={4} />
            <Bar dataKey="costs" fill="var(--color-costs)" radius={4} />
          </BarChart>
        </ChartContainer>
      </CardContent>
      {/* <CardFooter className="flex-col items-start gap-2 text-sm">
            <div className="flex gap-2 font-medium leading-none">
              Trending up by 5.2% this month <IconHome className="h-4 w-4" />
            </div>
            <div className="leading-none text-muted-foreground">
              Showing total visitors for the last 12 months
            </div>
          </CardFooter> */}
    </Card>
  )
}
