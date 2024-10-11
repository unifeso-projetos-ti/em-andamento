'use client'
import { NextUIProvider } from '@nextui-org/react'
import { NextIntlClientProvider } from 'next-intl'
import { ThemeProvider as NextThemesProvider } from 'next-themes'
import { Toaster } from 'react-hot-toast'

export const Provider = ({
  children,
  locale,
  messages,
}: {
  children: React.ReactNode
  locale: string
  messages: any
}) => {
  const timeZone = 'America/Brazil'

  return (
    <NextUIProvider locale="pt-BR">
      <Toaster position="top-right" />
      <NextIntlClientProvider
        timeZone={timeZone}
        locale={locale}
        messages={messages}
      >
        <NextThemesProvider attribute="class" defaultTheme="dark">
          {children}
        </NextThemesProvider>
      </NextIntlClientProvider>
    </NextUIProvider>
  )
}
