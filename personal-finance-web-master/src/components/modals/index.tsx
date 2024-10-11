import {
  Button,
  Modal,
  ModalBody,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalProps,
} from '@nextui-org/react'

interface ConfirmModalProps extends Omit<ModalProps, 'children'> {
  title: string
  message: string
  confirm?: string
  close?: string
  isOpen: boolean
  onClose: () => void
  onConfirm?: () => void // Função opcional para o clique de confirmação
}

export default function ConfirmModal({
  title,
  message,
  confirm,
  close,
  isOpen,
  onClose,
  onConfirm, // Recebe a função de confirmação
  ...modalProps
}: ConfirmModalProps) {
  return (
    <Modal isOpen={isOpen} onClose={onClose} {...modalProps}>
      <ModalContent>
        <>
          <ModalHeader className="flex flex-col gap-1">
            {title || 'Título Padrão'}
          </ModalHeader>
          <ModalBody>
            <p>{message || 'Mensagem Padrão'}</p>
          </ModalBody>
          <ModalFooter>
            <Button color="danger" variant="light" onPress={onClose}>
              {close || 'Fechar'}
            </Button>
            <Button
              color="primary"
              onPress={() => {
                if (onConfirm) {
                  onConfirm() // Chama a função de confirmação
                }
                onClose() // Fecha o modal
              }}
            >
              {confirm || 'Confirmar'}
            </Button>
          </ModalFooter>
        </>
      </ModalContent>
    </Modal>
  )
}
