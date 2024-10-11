import { getLocalTimeZone, parseDate } from '@internationalized/date'
import { useDateFormatter } from '@react-aria/i18n'

export function useFormattedDate() {
  const shortFormatter = useDateFormatter({ dateStyle: 'short' })
  const mediumFormatter = useDateFormatter({ dateStyle: 'medium' })
  const longFormatter = useDateFormatter({ dateStyle: 'long' })
  const fullFormatter = useDateFormatter({ dateStyle: 'full' })

  const formatDateString = (
    dateString: string | undefined | null, // Permitir valores undefined ou null
    dateStyle: 'short' | 'medium' | 'long' | 'full'
  ): string => {
    // Validação do dateString
    if (!dateString || typeof dateString !== 'string') {
      console.error('Invalid date string:', dateString)
      return '' // Ou retorne um valor padrão ou mensagem de erro apropriada
    }

    const isISOFormat = dateString.includes('T')
    let dateValue

    if (isISOFormat) {
      dateValue = new Date(dateString)
    } else {
      dateValue = parseDate(dateString)
    }

    const localDate =
      dateValue instanceof Date
        ? dateValue
        : dateValue.toDate(getLocalTimeZone())

    const formatter =
      dateStyle === 'long'
        ? longFormatter
        : dateStyle === 'medium'
          ? mediumFormatter
          : dateStyle === 'full'
            ? fullFormatter
            : shortFormatter

    return formatter.format(localDate)
  }

  return { formatDateString }
}
