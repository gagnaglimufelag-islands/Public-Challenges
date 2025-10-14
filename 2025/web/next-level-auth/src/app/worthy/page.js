"use client";
import Link from "next/link";
import { useSession, signOut } from "next-auth/react";

export default function NotWorthy() {
  const { data: session } = useSession();

  return (
    <div style={{ textAlign: "center", padding: "2rem" }}>
      {session ? (
        <>
          <h2 className="denied-title">You are not worthy! Try again if you dare!</h2>
          <Link href="/">
            <button
              className="denied-button"
              onClick={() => signOut({ callbackUrl: '/', redirect:true })}
            >
              Home
            </button>
          </Link>
        </>
      ) : (
        <>
          <h2 className="denied-title">You are not worthy! Try again if you dare!</h2>
          <Link href="/">
            <button className="denied-button">Home</button>
          </Link>
        </>
      )}
    </div>
  )
}