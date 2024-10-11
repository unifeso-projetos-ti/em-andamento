'use client'

import { doc, getDoc } from '@firebase/firestore'
import { zodResolver } from '@hookform/resolvers/zod'
import { Button, Input } from '@nextui-org/react'
import { signInWithEmailAndPassword } from 'firebase/auth'
import Image from 'next/image'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import { useState } from 'react'
import { SubmitHandler, useForm } from 'react-hook-form'
import { auth, firestore } from 'src/lib/firebase'
import { z } from 'zod'

export default function Home() {
  const router = useRouter()
  const [error, setError] = useState<string | null>(null)

  const validationSchema = z.object({
    email: z.string().min(1, { message: 'Email é obrigatório' }).email({
      message: 'Email inválido',
    }),
    password: z.string().min(1, 'Senha obrigatória'),
  })

  type Login = z.infer<typeof validationSchema>
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Login>({
    resolver: zodResolver(validationSchema),
  })

  const [loading, setLoading] = useState(false)

  const onSubmit: SubmitHandler<Login> = async (data) => {
    setLoading(true)
    setError(null)

    try {
      const userCredencial = await signInWithEmailAndPassword(
        auth,
        data.email,
        data.password
      )

      const user = userCredencial.user

      if (user.emailVerified) {
        const registrationData = localStorage.getItem('registrationData')

        const useDoc = await getDoc(doc(firestore, 'users', user.uid))
        console.log(useDoc)
        console.log(!useDoc.exists())

        if (!useDoc.exists()) {
          router.push('/costs')
        }
      }
    } catch (error) {
      if (error instanceof Error) {
        setError('Senha ou email inválidos')
      } else {
        setError('Senha ou email inválidos')
      }
      setLoading(false)
    }
  }

  return (
    <main className="h-screen w-screen">
      <div className="flex size-full bg-white lgMax:flex-col lgMax:gap-4">
        <div className="w-1/2 flex justify-center items-center lgMax:w-full p-4">
          <Image
            src={'/logo.svg'}
            width={32}
            height={32}
            alt="Moon"
            className="size-96 lgMax:size-32"
          />
        </div>
        <div className="w-1/2 size-full dark:bg-dark-background bg-light-background-navigation-bar flex flex-col items-center justify-center lgMax:w-full p-4 lgMax:rounded-t-3xl">
          <div className="flex flex-col  items-center justify-center rounded-xl p-8 border-1 lgMax:border-none lgMax:p-0">
            <header className="flex flex-col items-center mb-4 gap-2">
              <h1 className="text-4xl text-text-color">Entrar</h1>
              <Link className="text-white" href={'/'}>
                Não possui conta? Cadastre-se
              </Link>
            </header>

            <form
              onSubmit={handleSubmit(onSubmit)}
              className="flex flex-col items-start gap-5"
            >
              <Input
                {...register('email')}
                type="email"
                label="Email"
                placeholder="Insira o email"
                errorMessage={errors.email?.message}
                variant="faded"
              />
              <Input
                {...register('password')}
                errorMessage={errors.password?.message}
                type="password"
                label="Senha"
                placeholder="Insira a senha"
                variant="faded"
              />
              {/* <span className="flex justify-end w-full">
                <Link href={'/'}>Esqueceu sua senha?</Link>
              </span> */}

              {error && (
                <div
                  className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative"
                  role="alert"
                >
                  <span className="block sm:inline">{error}</span>
                </div>
              )}
              <Button
                type="submit"
                className="w-full"
                color="secondary"
                variant="shadow"
                isLoading={loading}
              >
                {loading ? '' : 'Entrar'}
              </Button>
            </form>
          </div>
        </div>
      </div>
    </main>
  )
}
