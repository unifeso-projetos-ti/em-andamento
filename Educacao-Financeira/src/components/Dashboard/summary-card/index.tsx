import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from 'src/components/ui/card'
import { ISummaryCard } from 'src/models/summary-card'
import { formatCurrency } from 'src/utils/currency'

export function SummaryCard({
  title,
  component,
  total,
  percentage,
  text_percentage,
}: ISummaryCard) {
  return (
    <Card className="w-[350px] p-0 bg-white">
      <CardHeader>
        <CardTitle className="flex items-center justify-between mb-2">
          <span>{title}</span> <div>{component}</div>
        </CardTitle>
        <div className="flex flex-col gap-2 mt-12">
          <CardDescription>
            <b className="text-xl">{formatCurrency(total)}</b>
          </CardDescription>
          <CardDescription>
            {percentage}% {text_percentage}
          </CardDescription>
        </div>
      </CardHeader>
    </Card>
  )
}
