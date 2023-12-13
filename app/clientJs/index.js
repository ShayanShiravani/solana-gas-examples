import anchor, { Wallet } from '@coral-xyz/anchor'
import { Keypair, Connection, clusterApiUrl } from '@solana/web3.js'
import { BN } from 'bn.js'
import 'dotenv/config'
import { readFileSync } from 'fs'

const opts = {
  preflightCommitment: "recent",
}

const idl = JSON.parse(
  readFileSync('./idl.json', 'utf8'),
)

const programId = new anchor.web3.PublicKey(process.env.PROGRAM_ID)

const testAccount = Keypair.fromSecretKey(Uint8Array.from(
  JSON.parse(process.env.SECRET_KEY)
))

const network = process.env.PROVIDER_URL || clusterApiUrl("testnet")
const connection = new Connection(network)
const wallet = new Wallet(testAccount)
const provider = new anchor.AnchorProvider(connection, wallet, opts)
anchor.setProvider(provider)

const latestBlockhash = await connection.getLatestBlockhash();

const program = new anchor.Program(idl, programId);

console.log('program: ', program.programId.toBase58())
console.log('wallet:', provider.wallet.publicKey.toBase58())

const logs = await program.methods.isPrime(new BN(24)).simulate()
console.log(logs.raw) 