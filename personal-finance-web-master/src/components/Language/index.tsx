'use client'

import { Button } from '@nextui-org/react'
import { useLocale } from 'next-intl'
import { useRouter } from 'next/navigation'
import { BrazilIcon } from '../Icons/BrazilIcon'
import { EnIcon } from '../Icons/EnIcon'

export const LangSelect = () => {
  const router = useRouter()
  const locale = useLocale()

  const toggleLocale = () => {
    const nextLocale = locale === 'pt' ? 'en' : 'pt'
    router.push(`/${nextLocale}`)
  }

  return (
    <Button className="bg-transparent p-2 outline-none" onClick={toggleLocale}>
      {locale === 'pt' ? <BrazilIcon /> : <EnIcon />}
    </Button>
  )
}
